var lastTweetID = undefined;

function startTwitterRefresh() {
    var default_interval = 300;

    function check_last_tweet() {
        var div = $("div.twitter-content iframe").contents().find("ol.timeline-TweetList > li:first > div");
        var newTweetID = div.attr("data-tweet-id");
        if ( lastTweetID === undefined ) {
            lastTweetID = newTweetID;
        }
        else if ( newTweetID !== lastTweetID ) {
            $("div.twitter-link i").addClass("blink");
            lastTweetID = newTweetID;
        }
    }

    setInterval(check_last_tweet, default_interval * 1000);
}

$(document).on("click", "div.twitter-link", function() {
    $("div.twitter-link i").removeClass("blink");
    $("div.twitter-content").slideToggle();
});
