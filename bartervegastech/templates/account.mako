# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Account</title>
</%def>

 <%def name="body()">

		<div id="main" class="container">
	
		<div class="row">
		
			<div id="account-main" class="twelve columns">
			
				<dl class="nice contained tabs">
				
					<dd><a href="#jobstab" class="active" title="Create or edit job posts">Add Job</a></dd>
					
					<dd><a class="" href="#profiletab" title="Edit your company profile">Edit Profile</a></dd>
					
				</dl>
				
				<ul class="nice tabs-content contained">
					
										<li style="display: block;" class="active" id="jobstabTab">
					
						<div class="row">
						
							<div class="seven columns">
							
															
								<h2><span>New job:</span> ${user.username}</h2>
								
								<p>Posts stay active for 45 days from the day they are posted. <br><span class="req">*</span> required.</p>
								
								${createpost | n}
							
							</div> 							
							<div id="active-posts" class="five columns">
							
																
								<a name="active-posts"></a>
								<h3>Active posts</h3>
								
								<p>Using <strong>${len(active)}</strong> of <strong>25</strong> available post slots.</p>
								
								<ul>
									%for each in active:
																				<li>
												<form name="active-post-${each.list_id}" id="active-post-${each.list_id}" method="post" action="/user/remove/${each.list_id}">
													<button type="button" name="delete" title="Delete this post" class="small white radius button nice" id="del-post-btn-${each.list_id}" onclick="$('#del-post-btn-${each.list_id}').hide(); $('#confirm-del-post-${each.list_id}').fadeIn(300); return false;">x</button>
													<button type="submit" name="confirm-delete" title="Delete this post" class="small red radius button nice acct-confirm-del" id="confirm-del-post-${each.list_id}">Confirm</button>
													<strong><a href="${each.url}" title="View job post">${each.title}</a></strong>
													<br>
													<span class="posted-on">Posted on ${each.date}</span>
												</form>
											</li>
									%endfor
																												
								</ul>
							
							</div> 						
						</div> 						
					</li>
					
										<li style="display: none;" id="profiletabTab">
					
												
												
						<span class="req-guide"><span class="req">*</span> Required</span>
						<h3>Edit company profile</h3>
						
						
												
						<form name="edit-profile" id="edit-profile-form" class="nice" method="post" action="">
						
							<div class="row">
							
								<div class="six columns">
								
									<label for="profile-company">Username <span class="req">*</span></label>
									<input class="expand input-text" id="profile-company" name="company" placeholder="username" value="${user.username}" maxlength="50" required="required" type="text">
																		
									<label for="profile-website">Website URL <span class="req">*</span></label>
									<input class="expand input-text" id="profile-website" name="website" placeholder="e.g. mysite.com" value="www.mysite.com" maxlength="100" required="required" type="text">
																		
									<label for="profile-tagline">Tag line or motto</label>
									<textarea name="tagline" id="profile-tagline" placeholder="ie. We make advanced web applications for the masses!" rows="3"></textarea>
									
									<label for="profile-twitter">Twitter username</label>
									<input class="expand input-text" id="profile-twitter" name="twitter" placeholder="ie. TwitterUser" maxlength="50" type="text">
									
								</div> 								
								<div class="six columns">
								
									<label for="profile-address1">Description</label>
									<textarea name="tagline" id="profile-tagline" placeholder="ie. We make advanced web applications for the masses!" rows="3"></textarea>
									
									<div id="edit-profile-submit-btns">
									
										<button type="submit" name="edit-profile-submit" id="edit-profile-submit" title="Update Profile" class="blue radius button nice">Update Profile</button>
									
									</div> 									
								</div> 								
							</div> 						
						</form>
					
					</li>
					
				</ul>
			
			</div> 		
		</div> 	
	</div> 
<script src="account_files/modernizr.js"></script>­<style>@media (touch-enabled),(-webkit-touch-enabled),(-moz-touch-enabled),(-o-touch-enabled),(-ms-touch-enabled),(modernizr){#touch{top:9px;position:absolute}}</style>
<script src="account_files/foundation.js"></script>
<script src="account_files/app.js"></script>
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
										
						<li><a href="/account" title="Account" id="current">Account</a></li>
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:										
						<li><a href="/users" title="User Section">Users</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif
 </%def>
 