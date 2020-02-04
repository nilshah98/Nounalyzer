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

  const percent = vals.map((val) => (val - valMin + 50) / (valMax - valMin));
  console.log(percent);

  const scaled = percent.map((p) => (p * (scaleMax - scaleMin)) + scaleMin);

  return scaled;

}

const getData = (feedURL) => {
    $.post("http://localhost:5000/rss",
    {
      rssLink: feedURL,
    },
    function(res, _status){

      const dataset = scaleVals(res.dataset);

      console.log(dataset);

      const svgHeight = 600, svgWidth = 600, barPadding = 5;
      const barWidth = svgWidth / dataset.length;

      // Resetting earlier content
      d3.selectAll('svg > *').remove();
      rssRes.innerHTML = "";

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
        .attr('fill', () => '#66CDAA')
        .transition()
        .duration(2000)
        .attr('transform', (d,i) => {
          const translate = [barWidth * i, -d];
          return `translate(${translate})`;
        })
        .style("opacity",0.6)

      console.log(res.feeds);
      rssRes.innerHTML += `</hr>`;
      for(let i=0; i<res.feeds.length; i++){
        rssRes.innerHTML += `<br/>`;
        rssRes.innerHTML += `<h4><strong>Title: </strong>${res.feeds[i]['title']}</h4>`;
        rssRes.innerHTML += `<br/>`;
        rssRes.innerHTML += `<p><strong>Summary: </strong> ${res.feeds[i]['summary']}</p>`;
        rssRes.innerHTML += `<a href='${res.feeds[i]['link']}'>Link</a>`;
        rssRes.innerHTML += `<hr/>`;
      }

    });
}