const getHen = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("hen");
        }, 5000);
    })  
  };
  
  const getEgg = (hen) => {
      return new Promise((resolve, reject) => {
          setTimeout(() => {
              resolve(`${hen} + => hen`);
          }, 1000);
      })
  };
  
  const cook = (egg) => {
      return new Promise((resolve, reject) => {
          setTimeout(() => {
              resolve(egg + "=> egg");
          }, 1000);
      })
  };
  
  getHen()
  .then(
      (value) => (getEgg(value))
  )
  .then (
      (value) => {console.log(value);}
  )