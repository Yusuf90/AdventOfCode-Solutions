const fs = require('fs');

fs.readFile('binarychart.txt', (err, data, dataPoint) => {
    if (err) throw err;

    dataPoint = data.toString().split('\n');
    const binaryChart = [];

    for (let i = 0; i < dataPoint.length; i++) {
        const element0 = dataPoint[i].split("");

        for (let j = 0; j < element0.length; j++) {
            const element1 = element0[j];
            
            if (i == 0) binaryChart[j] = [];
            binaryChart[j].push(element1)
        }
    }

    let mostAsString = '';
    for (const bc of binaryChart) {

        const most = bc.filter(index => index == 1).length > bc.filter(index => index == 0).length ? 1 : 0;
        mostAsString = mostAsString + most;
    }

    let mostArray = mostAsString.split('');

    const minArray = mostArray.map(ma => ma == '1' ? '0' : '1');

    const minAsString = minArray.join('');
    const minAsInt = parseInt(minAsString, 2);
    const mostAsInt = parseInt(mostAsString, 2);

    const res = minAsInt * mostAsInt;
    console.log(res);
})