/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
function timeLimit(fn, t) {
  return async function (...args) {
    return new Promise((resolve, reject) => {
      const timerId = setTimeout(() => reject("Time Limit Exceeded"), t)
      fn(...args)
      .then(res => resolve(res))
      .catch(reject)
      .finally(() => clearTimeout(timerId))
    })
  }
}
/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */