export let weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let epreqs = weakMap.get(endpoint) || 0;
  epreqs += 1;
  if (epreqs >= 5) throw Error('Endpoint load is high');
  weakMap.set(endpoint, epreqs);
}
