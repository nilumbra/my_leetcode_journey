async function sleep(millis: number): Promise<string> {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve("yjy"), millis)
    })
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */