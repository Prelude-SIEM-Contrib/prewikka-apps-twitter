<link rel="stylesheet" type="text/css" href="twitter/css/twitter.css">

<script type="text/javascript">
$(document).ready(function() {
    $LAB.script("twitter/js/twitter.js").wait(function() {
        startTwitterRefresh();
    });
});
</script>

<li>
    <div class="btn btn-default navbar-btn twitter-link">
        <i class="fa fa-twitter"></i>
    </div>
</li>

<div class="twitter-content" style="display:none">
    <a class="twitter-timeline"
      data-widget-id="${widget_id}"
      href="https://twitter.com/${account}"
      width="300">
    </a>

    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s) [0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>

</div>
