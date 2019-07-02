function buildMetadata(sample) {
  console.log("Build metadata"); 

  // @TODO: Complete the following function that builds the metadata panel
  var metadata = d3.select("#sample-metadata");
  var url = "/metadata/" + sample;
  d3.json(url).then(function(response) {
    metadata.html("");
    Object.entries(response).forEach(([k, v]) => metadata.append("p").text(`${k}: ${v}`));
  });
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {
  console.log("Build new chart");

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var url = "/samples/" + sample;
  d3.json(url).then(function(response){
    var ids = [];
    var values = [];
    var labels = [];
    for (i=0; i<10; i++){
      labels.push(response.otu_ids[i]);
      values.push(response.sample_values[i]);
      ids.push(response.otu_labels[i]);
    };
    var trace ={
      values: values,
      labels: labels,
      type: "pie",
      text: ids,
      textinfo: "percent"
    };
    var data = [trace];

    var pie = document.getElementById("pie");

    Plotly.newPlot(pie, data);
  });

  d3.json(url).then(function(response){
    var x = response.otu_ids;
    var y = response.sample_values;
    var z = response.sample_values;
    var colors = response.otu_ids;
    var labels2 = response.otu_labels;
    var trace2 = {
      x:x,
      y:y,
      mode:"markers",
      marker:{
        size:z,
        labels:labels2,
        color:colors
      }
    };

    var data2 = [trace2];
    Plotly.newPlot("bubble",data2);
  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
