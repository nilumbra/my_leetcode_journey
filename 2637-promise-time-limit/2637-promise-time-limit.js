function timeLimit(fn, t) {
  return async function (...args) {
    const timeOutPromise = new Promise((_, reject) => {
      setTimeout(() => reject("Time Limit Exceeded"), t)
    })
    const returnedPromise = fn(...args) 
    return Promise.race([timeOutPromise, returnedPromise])
  }
}