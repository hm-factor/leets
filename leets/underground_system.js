
var UndergroundSystem = function() {
//     if checkin doesnt exist, create one with key of id and value of time
    this.checkIns = {};
//     when someone travels from a location, create key of starting place and value should be a hash with keys of endpoints and values of arrays of time, (that way an avg can be easily taken)
    this.travelTime= {};
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
  this.checkIns[id] = [stationName, t];
  if (!this.travelTime[stationName]){
    this.travelTime[stationName] = {};
  }
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    if(this.checkIns[id]) {
        let [start, time] = this.checkIns[id]
        if(Array.isArray(this.travelTime[start][stationName])) {
            this.travelTime[start][stationName].push(t - time)
        } else {
            this.travelTime[start][stationName] = [t - time]
        }
    } else return null
};

/** 
 * @param {string} startStation 
 * @param {string} endStation
 * @return {number}
 */
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    let arr = this.travelTime[startStation][endStation];
    if (!arr) return null;
    let len = arr.length;
    console.log(this.travelTime)
    let sum = arr.reduce(((acc, val) => acc + val), 0);
    return sum/len
};

/** 
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */