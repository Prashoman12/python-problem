// const numbers = [1, 2, 2, 3];

// const uniqueNumbers = numbers.filter((value, index, self) => {
//   console.log("Value:", value, "Index:", index, "Self:", self, "IndexOf(value):", self.indexOf(value));
//   return self.indexOf(value) === index;
// });
// console.log(uniqueNumbers)

const numbers = [1, 2, 2, 3, 4, 4, 5];
const uniqueNumbers = [];

for (let i = 0; i < numbers.length; i++) {
  if (!uniqueNumbers.includes(numbers[i])) {
    uniqueNumbers.push(numbers[i]);
  }
}

console.log(uniqueNumbers); 
