#!/usr/bin/node
exports.esrever = function (list) {
  let j = 0;
  const finalList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    finalList[j] = list[i];
    j++;
  }
  return (finalList);
};
