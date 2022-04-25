/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    function reverse1(start: number, end: number, s: string[]) {
        if (start > end) return;
        const t: string = s[start];
        s[start] = s[end];
        s[end] = t;
        
        reverse1(start + 1, end - 1, s)
    }

    reverse1(0, s.length - 1, s)
};