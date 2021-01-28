// Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

// Implement the LRUCache class:

// LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
// int get(int key) Return the value of the key if the key exists, otherwise return null.
// void put(key (int), value) Update the value of the key if the key exists. Otherwise, 
// add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

// initialize(size) __init__(self):
// get(key) -> value | null
// put(key, value) -> null

// Map 

class LRUCache {
  constructor(size) {
    this.size=size;
    this.cache={};
    this.order=[];
  }

  // {1:1, 3:3}
  // [1,3]

  put(k, v) {
    // k,v pair is put into cache
    // k is put into order
    this.cache[k] = v;

    let currIdx = this.order.indexOf(k); 
    if(currIdx >= 0) this.order.slice(currIdx, 1);
    this.order.push(k);

    // if order exceeds size, shift first element off
    // if key exists in cache, then update k,v pair, and update place in order (relevancy)

    if(this.size < this.order.length()) {
      this.order.shift();
      delete this.cache.k;
    }
  }

  get(k) {
    if(k in this.cache) {
      let currIdx = this.order.indexOf(k);
      this.order.splice(currIdx, 1);
      this.order.push(k);

      return this.cache[k];
    } else {
      return null;
    }
    // find index of k, slice k from order, push k onto order
    // acquire corresponding value for k or return null if nonexistent
    // key in object -> boolean HACKS
  }
}

// LRUCache lRUCache = new LRUCache(2);
// lRUCache.put(1, 1); // cache is {1=1}
// lRUCache.put(2, 2); // cache is {1=1, 2=2}
// lRUCache.get(1);    // return 1
// lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
// lRUCache.get(2);    // returns null (not found)


// put(1, 11)
// put(2, 22)

// { 1: 11, 2: 22 }
//  [1, 2]

// https://leetcode.com/problems/lru-cache/