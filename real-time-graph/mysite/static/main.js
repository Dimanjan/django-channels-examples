const ctx = document.getElementById('myChart').getContext('2d');

let graphData={
    type: 'line',
    data: {
        labels: ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(73, 199, 232, 0.5)',
            ],
            borderWidth: 1
        },
    
        {fill: {
            target: 'origin',
            above: 'rgb(255, 0, 0)',   // Area will be red above the origin
            below: 'rgb(0, 0, 255)'    // And blue below the origin
          }}]
    },
    options: {}
}
const myChart = new Chart(ctx,graphData );


let socket=new WebSocket(`ws://${window.location.host}/ws/graph/`);

socket.onmessage=function(e){
    let data=JSON.parse(e.data)

    var newGraphData=graphData.data.datasets[0].data;
    newGraphData.shift();
    newGraphData.push(data.value);
    graphData.data.datasets[0].data=newGraphData;

    myChart.update();

}