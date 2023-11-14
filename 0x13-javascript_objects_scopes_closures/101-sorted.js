#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
const keyList = [];
Object.keys(dict).forEach(key => {
  const value = dict[key];
  if (newDict[value] === undefined) {
    newDict[value] = [];
  }
  keyList.push(key);
});
for (const key of keyList) {
  const value = dict[key];
  newDict[value].push(key);
}
console.log(newDict);
