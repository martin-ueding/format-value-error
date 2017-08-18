# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see http://www.gnu.org/licenses/.
#
# This file is in UTF-8 encoding.

# -*- texinfo -*-
# @deftypefn {Function File} unitprint (@var{data})
#
# Prints the associated value and error with the given unit.
#
# It assumes that there is a @var{data.val} in the struct @var{data} that is
# given as a parameter. If there is a @var{data.unit}, that will be displayed.
# If there is a @var{data.err} key, it will be displayed with the relative
# error.
#
# If @var{data.lit} it given, the deviation from the literature value is
# calculated and displayed also. If @var{data.err} is present, it will be
# checked, whether the measurement is close enough to the literature value. If
# so, it will display a checkmark, a cross otherwise.
#
# It will print data like this:
#
# @code{name = value \pm error (relative error) unit [deviation checkmark]}
#
# @end deftypefn

function unitprint(data)
	if isfield(data, "name")
		printf("%s = ", data.name)
	endif

	printf("%.3g ", data.val)

	if isfield(data, "err")
		printf(" ± %.2g", data.err)
		printf(" (%.2g)", data.err / data.val)
	endif

	if isfield(data, "unit")
		printf(" %s", data.unit)
	endif

	# If there is a literature (i. e. canonical reference) value, print that as
	# well.
	if isfield(data, "lit")
		printf(" [%.2g", (data.val - data.lit) / data.lit)

		# If there is an error margin given, check whether the the canonical
		# value fits into there.
		if isfield(data, "err")
			if abs(data.val - data.lit) <= data.err
				printf(" ✓")
			else
				printf(" ✗")
			endif
		endif

		printf("]");
	endif

	printf("\n")
endfunction
