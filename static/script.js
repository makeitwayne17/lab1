var color1 = '#9966ff';
var color2 = '#428bca';
var color3 = '#5cb85c';
var color4 = '#d9534f';
var color5 = '#fc9c36';

var options = {
	scales: {
		yAxes: [{
			ticks: {
				beginAtZero: true
			}
		}],
		xAxes: [{
			ticks: {
				maxTicksLimit: 12
			}
		}]
	},
	responsive: false
}

function load() {
	var readings = JSON.parse(data);
	generateChart(readings);
}

function generateChart(readings) {

	// sets up y-axis as interval [0, 60)
	var timeframe = [];
	for (var i = 0; i < 60; i++) {
		timeframe.push(i);
	}

	var ctx = document.getElementById("chart1").getContext('2d');
	var myLineChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: timeframe,
			datasets: [{
				label: 'Temperature',
				data: readings.temp,
				backgroundColor: color1,
				borderColor: color1,
				fill: false,
				borderWidth: 1
			}, {
				label: 'Humidity',
				data: readings.humidity,
				backgroundColor: color2,
				borderColor: color2,
				fill: false,
				borderWidth: 1
			}]
		},
		options: options
	});

	var ctx = document.getElementById("chart2").getContext('2d');
	var myLineChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: timeframe,
			datasets: [{
				label: 'Audio',
				data: readings.audio,
				backgroundColor: color3,
				borderColor: color3,
				fill: false,
				borderWidth: 1
			}]
		},
		options: options
	});

	var ctx = document.getElementById("chart3").getContext('2d');
	var myLineChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: timeframe,
			datasets: [{
				label: 'Envelope',
				data: readings.envelope,
				backgroundColor: color4,
				borderColor: color4,
				fill: false,
				borderWidth: 1
			}]
		},
		options: options
	});

	var ctx = document.getElementById("chart4").getContext('2d');
	var myLineChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: timeframe,
			datasets: [{
				label: 'Gate',
				data: readings.gate,
				backgroundColor: color5,
				borderColor: color5,
				fill: false,
				borderWidth: 1
			}]
		},
		options: options
	});

}