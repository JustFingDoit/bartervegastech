# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: ${listing.title}</title>
</%def>
<%def name="body()">

		<div id="main" class="container">
	
		<div class="row">
		
			<div id="job-body" class="nine columns">
			
								<ul class="breadcrumbs">
				
					<li><a href="javascript:history.back()" title="Back">Back</a></li>
					<li><a href="/" title="Home" id="breadcrumb-home">Home</a></li>
					<li class="unavailable"><a href="#">${listing.username}</a></li>
					<li class="current hide-on-phones"><a href="#">${listing.title}</a></li>
					
				</ul>
				
				<h1>${listing.title}</h1>
				<h2><span>from</span> ${listing.username}</h2>
				
				<div id="job-meta" class="panel">
					
					<ul class="block-grid two-up">
					
						<li>
						
							<p>Posted: <strong>${listing.date}</strong>
						
							</p><p>Status: <strong>${listing.type}</strong></p>
					
							<p>Category: <strong>${listing.category}</strong></p>
						
						</li>
						
						<li>
							
							<p></p>
							
							<p></p>
							
							<p></p>
							
						</li>
					
					</ul>
					
				</div> 				
				<div id="job-description" class="panel">
				
					<h5>Description</h5>
				
					<p>${listing.description}</p>
				
				</div> 				
				<div id="job-howtoapply" class="panel">
				
					<h5>In Return</h5>
				
					<p>${listing.inreturn}</p>
				
				</div>
				%for each in replies:
				<div id="reply" class="panel">
				
					<h5>${each.user.username}:</h5>
				
					<p>${each.description}</p>
				
				</div>
				%endfor
				%if request.session.get('logged_in') != None and request.session.get('logged_in') >= 0:
				<div id="job-reply" class="panel">
				%if private:
					<h5>Private Reply - you should let them know how to contact you</h5>
				%else:
					<h5>Reply - If necessary you should let them know how to contact you</h5>
				%endif					
					<form name='reply' action='' method='post'>
					<p><textarea name='description' class='expand' rows='10'>Your reply</textarea></p>
					<p><button type="submit" name="reply" id="job-submit-btn" class="nice blue radius button">Reply</button></p>
					
					</form>
				</div>
				%endif 			
			</div> 			
			<div id="job-sidebar" class="three columns">
			
								<h6>${listing.username}</h6>
			%if listing.user.website != None and listing.user.website != 'None':
									<p>Website: ${listing.user.website}</p>
			%endif
			%if listing.user.tagline != None and listing.user.tagline != 'None':					
									<p>Tagline: ${listing.user.tagline}</p>
			%endif
			%if listing.user.twitter != None and listing.user.twitter != 'None':					
									<p>Twitter: <a href='http://www.twitter.com/#/${listing.user.twitter}'>${listing.user.twitter}</a></p>
			%endif
			%if listing.user.description != None and listing.user.description != 'None':					
									<p>Description: ${listing.user.description}</p>
			%endif

				<div id="job-post-share">
					<strong>Share this:</strong>
					<br>
					<!-- AddThis Button BEGIN -->
					<div class="addthis_toolbox addthis_default_style ">
					<a href="http://www.addthis.com/bookmark.php?v=250&amp;pubid=xa-4f83ad462e1f9116" class="addthis_button_compact at300m"><span class="at16nc at300bs at15nc at15t_compact at16t_compact"><span class="at_a11y">More Sharing Services</span></span>Share</a>
					<span class="addthis_separator">|</span>
					<a href="#" title="Send to Facebook" class="addthis_button_preferred_1 addthis_button_facebook at300b"><span class="at16nc at300bs at15nc at15t_facebook at16t_facebook"><span class="at_a11y">Share on facebook</span></span></a>
					<a href="#" title="Tweet This" class="addthis_button_preferred_2 addthis_button_twitter at300b"><span class="at16nc at300bs at15nc at15t_twitter at16t_twitter"><span class="at_a11y">Share on twitter</span></span></a>
					<a href="#" title="Email" class="addthis_button_preferred_3 addthis_button_email at300b"><span class="at16nc at300bs at15nc at15t_email at16t_email"><span class="at_a11y">Share on email</span></span></a>
					<a href="#" title="Print" class="addthis_button_preferred_4 addthis_button_print at300b"><span class="at16nc at300bs at15nc at15t_print at16t_print"><span class="at_a11y">Share on print</span></span></a>
					<div class="atclear"></div></div>
					<script type="text/javascript" src="/js/addthis_widget.js"></script>
					<!-- AddThis Button END -->
				
				</div> 			
			</div> 		
		</div> 	
	</div> 
<script src="/js/modernizr.js"></script>­<style>@media (touch-enabled),(-webkit-touch-enabled),(-moz-touch-enabled),(-o-touch-enabled),(-ms-touch-enabled),(modernizr){#touch{top:9px;position:absolute}}</style>
<script src="/js/foundation.js"></script>
<script src="/js/app.js"></script>
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
					
					<li><a href="/about" title="About #VegasTech">About</a></li>
					
%if request.session.get('logged_in') != None and request.session.get('logged_in') >= 0:
										
						<li><a href="/account" title="Account" >Account</a></li>
						
						<li><a href="http://www.hirevegastech.com" title="HireVegasTech.com - Free job board for #VegasTech" target="_blank" class="has-tip">Hire</a></li>
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:										
						<li><a href="/users" title="User Section">Users</a></li>
						
						<li><a href="http://www.hirevegastech.com" title="HireVegasTech.com - Free job board for #VegasTech" target="_blank" class="has-tip">Hire</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif	
 </%def>