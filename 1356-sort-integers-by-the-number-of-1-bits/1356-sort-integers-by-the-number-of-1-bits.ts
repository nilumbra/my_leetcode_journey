function sortByBits(arr: number[]): number[] {
    return arr.sort((a, b) => bits(a) - bits(b) || a - b)
};

function bits(n: number): number {
    return [...n.toString(2)].reduce((sum, char) => char === '1' ? sum + 1 : sum, 0)
}