//import data from txt file, transform into array
const fs = require('fs');

fs.readFile('directionchart.txt', (err, data, directionPoints) => {
    if (err) throw err;

    directionPoints = data.toString().split('\n');
    let forwardInputs = 0;
    let upwardInputs = 0;
    let downwardInputs = 0;

    for (let i=0; i < directionPoints.length; i++) {
        currentValue = parseInt(directionPoints[i].slice(-1));
        switch(directionPoints[i][0]) {
            case 'u':    
                upwardInputs = upwardInputs + currentValue;
                break;
            case 'd':
                downwardInputs = downwardInputs + currentValue;
                break;
            case 'f':
                forwardInputs = forwardInputs + currentValue;
                break;
            default:
                return;
        }
    }

    console.log(`input coordinates forward: ${forwardInputs}`);
    console.log(`input coordinates upward: ${upwardInputs}`);
    console.log(`input coordinates downward: ${downwardInputs}`);

    let movementY = downwardInputs - upwardInputs;
    let movementX = forwardInputs;

    totalMovement = movementX * movementY;
    console.log(`totalMovement: ${totalMovement}`);
})

//get all keys for forward, backward, up, down

//calculate sum of each

//extrapolate forward-backward and down-up

//calculate x * y