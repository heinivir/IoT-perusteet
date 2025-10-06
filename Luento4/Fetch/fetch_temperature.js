const url = "https://api.thingspeak.com/channels/3081115/feeds.json?results=20";

let chart; 

async function fetchData() {
  try {
    const response = await fetch(url);
    const data = await response.json();
    const feeds = data.feeds;

    const labels = feeds.map(feed => new Date(feed.created_at).toLocaleTimeString());
    const temps = feeds.map(feed => parseFloat(feed.field1));

    //document.getElementById("output").textContent = JSON.stringify(feeds, null, 2);

    if (!chart) {

      const ctx = document.getElementById("temperatureChart").getContext("2d");
      chart = new Chart(ctx, {
        type: "line",
        data: {
          labels: labels,
          datasets: [{
            label: "Temperature (°C)",
            data: temps,
            borderColor: "blue",
            backgroundColor: "rgba(0, 0, 255, 0.1)",
            fill: true,
            tension: 0.2
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: true },
            title: { display: true, text: "Temperature over Time" }
          },
          scales: {
            x: { title: { display: true, text: "Time" } },
            y: { title: { display: true, text: "°C" } }
          }
        }
      });
    } else {
      chart.data.labels = labels;
      chart.data.datasets[0].data = temps;
      chart.update();
    }
  } catch (error) {
    console.error("Error fetching data", error);
    document.getElementById("output").textContent = "Error loading data";
  }
}

fetchData();


setInterval(fetchData, 30000);
