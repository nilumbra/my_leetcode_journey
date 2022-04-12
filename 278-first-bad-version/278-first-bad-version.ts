/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {

    return function(n: number): number {
        let start: number = 0,
            end: number = n;
        while (start <= end) {
            const middle: number = Math.floor((end - start) / 2) + start;
            if (!isBadVersion(middle)) start = middle + 1;
            else if (isBadVersion(middle) && isBadVersion(middle - 1)) end = middle - 1;
            else return middle;
	}
    };
};