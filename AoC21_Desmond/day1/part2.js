const fs = require('fs')

function checkDepth() {
    let deeperPoints = 0;

    fs.readFile('depthchart.txt', (err, data, dataPoints) => {
        if (err) throw err;

        dataPoints = data.toString().split('\n');

        let prevTotalDepth = parseInt(dataPoints[0]) + parseInt(dataPoints[1]) + parseInt(dataPoints[2]); 
      
        for (let i=0; i < dataPoints.length - 2; i++) {
         
            const idx0 = parseInt(dataPoints[i]);
            const idx1 = parseInt(dataPoints[i + 1]);
            const idx2 = parseInt(dataPoints[i + 2]);
            const totalDepth = (idx0 + idx1 + idx2);
   
            if(totalDepth > prevTotalDepth) {
                deeperPoints++;
            }

            prevTotalDepth = totalDepth

            
        }

        console.log(deeperPoints);
    })

}
checkDepth();



