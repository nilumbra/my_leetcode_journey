function largestAltitude(gain: number[]): number {
    let altitude = 0
    let highest = 0
    for (const g of gain) {
        altitude += g
        highest = Math.max(altitude, highest)
    }
    
    return highest
};