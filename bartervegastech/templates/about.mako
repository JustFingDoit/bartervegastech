# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: About</title>
</%def>

 <%def name="body()">

		<div id="about-topper" class="container">
	
		<div class="row">
		
			<div id="about-feature" class="twelve columns">
			
				<div class="hide-on-phones">
				
					<span id="about-topper-quote">"It's not Silicon Valley. That's a <em>good</em> thing."</span><br><span id="about-topper-credit">From <a href="http://gigaom.com/2012/02/17/for-startups-las-vegas-is-a-beautifully-clean-slate/" title="Read 'For startups, Las Vegas is a beautifully clean slate' on GigaOM" class="article" target="_blank">For startups, Las Vegas is a beautifully clean slate</a> on <strong><a href="http://www.gigaom.com/" title="GigaOM" id="gigaom-link" target="_blank">GigaOM</a></strong></span>
					
				</div> 				
				<div class="show-on-phones">
				
					<span id="about-topper-quote-mobile">"It's not Silicon Valley. That's a <em>good</em> thing."</span><br><span id="about-topper-credit-mobile">From <a href="http://gigaom.com/2012/02/17/for-startups-las-vegas-is-a-beautifully-clean-slate/" title="Read 'For startups, Las Vegas is a beautifully clean slate' on GigaOM" class="article" target="_blank">For startups, Las Vegas is a beautifully clean slate</a> on <strong><a href="http://www.gigaom.com/" title="GigaOM" id="gigaom-link-mobile" target="_blank">GigaOM</a></strong></span>
					
				</div> 			
			</div> 		
		</div> 	
	</div> 	
		<div id="main" class="container">
	
		<div class="row">
		
			<div id="about-main" class="eight columns">
			
				<div class="panel hide-on-phones">
					
					<p class="big"><strong class="blue">Hire</strong>#<strong class="red">VegasTech</strong> is a <em>free</em>
 job board for designers, programmers, and other web or technology 
professionals in Las Vegas, Nevada. Created for, and inspired by, the 
amazing <a href="https://twitter.com/#%21/search/%23VegasTech" id="vt-hash-link" class="has-tip tip-top" data-width="180" title="Follow the #VegasTech hashtag on Twitter" target="_blank">#VegasTech</a> scene!</p>
					
				</div> 				
				<div class="panel show-on-phones">
					
					<p class="big-mobile"><strong class="blue">Hire</strong>#<strong class="red">VegasTech</strong> is a <em>free</em>
 job board for designers, programmers, and other web or technology 
professionals in Las Vegas, Nevada. Created for, and inspired by, the 
amazing <a href="https://twitter.com/#%21/search/%23VegasTech" title="Follow the #VegasTech hashtag on Twitter" target="_blank">#VegasTech</a> scene!</p>
					
				</div> 				
				<p id="post-notice">Want something? <a href="/users" title="Create a free post">Create a post</a> - it's quick and easy (we promise)!</p>
			
			</div> 			
			<div id="about-side" class="four columns">
			
				<h2>Other #VegasTech Resources</h2>
				
				<ul>
					
					<li>
						
						<h4>Vegas Tech <a href="http://vegastech.com/" title="Vegas Tech" target="_blank">vegastech.com</a></h4>
						
						<p>Meet some of the talent and startups behind the growing tech scene in Las Vegas</p>
						
					</li>
					
					<li>
						
						<h4>Las Vegas Startups <a href="http://vegasstartups.com/" title="Las Vegas Startups - Rick Duggan" target="_blank">vegasstartups.com</a></h4>
						
						<p>Startup news from #VegasTech's Rick Duggan (<a href="http://twitter.com/rickduggan" class="has-tip tip-top" title="Follow Rick on Twitter" target="_blank">@rickduggan</a>) and John Lynn (<a href="http://twitter.com/techguy" class="has-tip tip-top" title="Follow John on Twitter" target="_blank">@techguy</a>)</p>
						
					</li>
					
					<li>
						
						<h4>Las Vegas Jelly <a href="http://vegasjelly.com/" title="Las Vegas Jelly" target="_blank">vegasjelly.com</a></h4>
						
						<p>Casual co-working and weekly meetings every Thursday in downtown Las Vegas</p>
						
					</li>
					
					<li>
						
						<h4>/usr/lib <a href="http://usrlib.org/" title="/usr/lib co-working space" target="_blank">usrlib.org</a></h4>
						
						<p>Community tech library, co-working hangout and meet-up venue in downtown Las Vegas</p>
						
					</li>
					
				</ul>
			
			</div> 		
		</div> 		
	</div> 
<script src="about_files/modernizr.js"></script>­<style>@media (touch-enabled),(-webkit-touch-enabled),(-moz-touch-enabled),(-o-touch-enabled),(-ms-touch-enabled),(modernizr){#touch{top:9px;position:absolute}}</style>
<script src="about_files/foundation.js"></script>
<script src="about_files/app.js"></script>
<script>
$(function(){
	$('#modal-login-link').click(function(e){
		e.preventDefault();
		$('#nav-modal').trigger('reveal:close');
		$('#login-modal').reveal({
			animation: 'fade'
		});
	});
	$('#close-login-modal-reveal').click(function(e){
		e.preventDefault();
		$('#login-modal').trigger('reveal:close');
	});
});
</script>

 </%def>
 

 <%def name="navlinks()">
 					<li><a href="/" title="Home">Home</a></li>
					
					<li><a href="/about" title="About #VegasTech" id="current">About</a></li>
					
										
						<li><a href="/users" title="User Section">Users</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
 </%def>

