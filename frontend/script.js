const rss = document.getElementById("rss");
const rssName = document.getElementById("rss__name");
const rssRes = document.getElementById("res__content");

rss.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log(rssName.value);
    getData(rssName.value);
})

const getData = (feedURL) => {
    $.post("http://localhost:5000/rss",
    {
      rssLink: feedURL,
    },
    function(data, status){
      rssRes.textContent = `Data: ${data} Status: ${status}`;
    });
}