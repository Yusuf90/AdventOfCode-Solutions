const fs = require('fs')

function checkDepth() {
    let deeperPoints = 1;

    fs.readFile('depthchart.txt', (err, data, dataPoints) => {
        if (err) throw err;

        dataPoints = data.toString().split('\n');

        for (let i=0; i < dataPoints.length; i++) {

            if(dataPoints[i] < dataPoints[i + 1]) {
                deeperPoints++;
            }
        }
    
        console.log(deeperPoints);
    })

}
checkDepth();



