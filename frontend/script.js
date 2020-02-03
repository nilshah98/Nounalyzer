const rss = document.getElementById("rss");
const rssName = document.getElementById("rss__name");
const rssRes = document.getElementById("res__content");

rss.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log(rssName.value);
    getData(rssName.value);
})

const scaleVals = (vals) => {
  const scaleMin = 0;
  const scaleMax = 500;

  const valMin = Math.min(...vals);
  const valMax = Math.max(...vals);

  const percent = vals.map((val) => (val - valMin) / (valMax - valMin));
  console.log(percent);

  const scaled = percent.map((p) => (p * (scaleMax - scaleMin)) + scaleMin);

  return scaled;

}

const getData = (feedURL) => {
    $.post("http://localhost:5000/rss",
    {
      rssLink: feedURL,
    },
    function(res, status){
      rssRes.textContent = `Data: ${res} Status: ${status}`;

      const dataset = scaleVals(res.data);

      console.log(dataset);

      const svgHeight = 600, svgWidth = 600, barPadding = 5;
      const barWidth = svgWidth / dataset.length;

      d3.selectAll('svg > *').remove();

      var svg = d3.select('svg')
        .attr('width', svgWidth)
        .attr('height', svgHeight)

      var barChart = svg.selectAll('rect')
        .data(dataset)
        .enter()
        .append('rect')
        .attr('y', (d) => svgHeight)
        .attr('height', (d) => d)
        .attr('width', barWidth - barPadding)
        .attr('class', 'bar')
        .attr('transform', (d,i) =>{
          const translate = [barWidth * i];
          return `translate(${translate})`;
        })
        .transition()
        .duration(300)
        .attr('transform', (d,i) => {
          const translate = [barWidth * i, -d];
          return `translate(${translate})`;
        })

      

    });
}