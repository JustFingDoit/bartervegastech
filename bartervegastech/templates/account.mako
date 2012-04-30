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
							
															
								<h2><span>New job:</span> Versogroup</h2>
								
								<p>Jobs posts stay active for 45 days from the day they are posted. <br><span class="req">*</span> required.</p>
								
								<form name="post-job" id="post-job" class="nice" method="post" action="">
								
									<label for="position">Position Title <span class="req">*</span></label>
									<input class="expand input-text" id="position" name="position" required="required" maxlength="100" placeholder="ie. Sr. Web Designer" type="text">
																		
									<label for="status">Status <span class="req">*</span></label>
									<select name="status" id="status">
										<option selected="selected" value="full-time">Full Time</option>
										<option value="part-time">Part Time</option>
										<option value="freelance">Freelance</option>
										<option value="contract">Contract</option>
									</select>
																		
									<label for="duration">Duration</label>
									<input class="expand input-text" id="duration" name="duration" maxlength="150" placeholder="ie. Ongoing" type="text">
									
									<label for="starts">Starts <span class="req">*</span></label>
									<input class="expand input-text" id="starts" name="starts" maxlength="150" placeholder="ie. ASAP" type="text">
																		
									<label for="rate">Rate or Salary <span class="req">*</span></label>
									<input class="expand input-text" id="rate" name="rate" maxlength="100" placeholder="ie. $60K to $80K DOE" type="text">
																		
									<label for="category">Category <span class="req">*</span></label>
									<select name="category" id="category">
										<option selected="selected" value="null">Please choose:</option>
										<option value="design">Design</option>
										<option value="programming">Programming</option>
										<option value="information-tech">Information Technology</option>
										<option value="engineering">Engineering</option>
										<option value="other">Other</option>
									</select>
																		
									<label for="description">Description <span class="req">*</span><span class="note">No HTML</span></label>
									<textarea name="description" id="description" class="expand" placeholder="Include a brief description of your company, position responsibilities, and skill requirements..." rows="10" required="required"></textarea>
																		
									<label for="howtoapply">How to Apply <span class="req">*</span><span class="note">No HTML</span></label>
									<textarea name="howtoapply" id="howtoapply" class="expand" placeholder="Include URL or email address along with any applicable instructions for the candidate" rows="4" required="required"></textarea>
																		
									<div id="post-job-submit">
									
										<button type="submit" name="job-submit-btn" id="job-submit-btn" class="nice blue radius button">Submit Job</button>
									
									</div> 								
								</form>
							
							</div> 							
							<div id="active-posts" class="five columns">
							
																
								<a name="active-posts"></a>
								<h3>Active posts</h3>
								
								<p>Using <strong>3</strong> of <strong>25</strong> available post slots.</p>
								
								<ul>
									
																				<li>
												<form name="active-post-31" id="active-post-31" method="post" action="">
													<button type="button" name="delete" title="Delete this post" class="small white radius button nice" id="del-post-btn-31" onclick="$('#del-post-btn-31').hide(); $('#confirm-del-post-31').fadeIn(300); return false;">x</button>
													<button type="submit" name="confirm-delete" title="Delete this post" class="small red radius button nice acct-confirm-del" id="confirm-del-post-31">Confirm</button>
													<input name="jid" value="31" type="hidden">
													<strong><a href="http://hirevegastech.com/job/versogroup/2012-04-20/design/full-time/web-designer/" title="View job post">Web designer</a></strong>
													<br>
													<span class="posted-on">Posted on Apr 202012</span>
												</form>
											</li>
																					<li>
												<form name="active-post-29" id="active-post-29" method="post" action="">
													<button type="button" name="delete" title="Delete this post" class="small white radius button nice" id="del-post-btn-29" onclick="$('#del-post-btn-29').hide(); $('#confirm-del-post-29').fadeIn(300); return false;">x</button>
													<button type="submit" name="confirm-delete" title="Delete this post" class="small red radius button nice acct-confirm-del" id="confirm-del-post-29">Confirm</button>
													<input name="jid" value="29" type="hidden">
													<strong><a href="http://hirevegastech.com/job/versogroup/2012-04-20/programming/full-time/developers-developers-developers-developers-developers-developers/" title="View job post">Developers Developers Developers Developers Developers Developers </a></strong>
													<br>
													<span class="posted-on">Posted on Apr 202012</span>
												</form>
											</li>
																					<li>
												<form name="active-post-9" id="active-post-9" method="post" action="">
													<button type="button" name="delete" title="Delete this post" class="small white radius button nice" id="del-post-btn-9" onclick="$('#del-post-btn-9').hide(); $('#confirm-del-post-9').fadeIn(300); return false;">x</button>
													<button type="submit" name="confirm-delete" title="Delete this post" class="small red radius button nice acct-confirm-del" id="confirm-del-post-9">Confirm</button>
													<input name="jid" value="9" type="hidden">
													<strong><a href="http://hirevegastech.com/job/Versogroup/2012-04-10/other/part-time/n00b-level-social-media-/" title="View job post">n00b level social media </a></strong>
													<br>
													<span class="posted-on">Posted on Apr 102012</span>
												</form>
											</li>
																												
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
								
									<label for="profile-company">Company name <span class="req">*</span></label>
									<input class="expand input-text" id="profile-company" name="company" placeholder="ie. My Company" value="Versogroup" maxlength="50" required="required" type="text">
																		
									<label for="profile-website">Website URL <span class="req">*</span></label>
									<input class="expand input-text" id="profile-website" name="website" placeholder="ie. company.com" value="www.versogroup.com" maxlength="100" required="required" type="text">
																		
									<label for="profile-tagline">Tag line or motto</label>
									<textarea name="tagline" id="profile-tagline" placeholder="ie. We make advanced web applications for the masses!" rows="3"></textarea>
									
									<label for="profile-twitter">Twitter username</label>
									<input class="expand input-text" id="profile-twitter" name="twitter" placeholder="ie. TwitterUser" maxlength="50" type="text">
									
								</div> 								
								<div class="six columns">
								
									<label for="profile-address1">Street address</label>
									<input class="expand input-text" name="address_1" id="profile-address1" placeholder="ie. 123 Main Street" maxlength="100" type="text">
									<input class="expand input-text" name="address_2" id="profile-address2" placeholder="ie. Suite 300" maxlength="100" type="text">
									
									<label for="profile-city">City</label>
									<input class="expand input-text" id="profile-city" name="city" placeholder="ie. Las Vegas" maxlength="50" type="text">
									
									<label for="profile-city">State</label>
									<input class="expand input-text" id="profile-city" name="state" value="Nevada" maxlength="50" disabled="disabled" type="text">
									
									<label for="profile-zipcode">Zipcode</label>
									<input class="input-text" id="profile-zipcode" name="zipcode" placeholder="ie. 89101" maxlength="10" type="text">
									
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
					
%if items['logged_in']:
										
						<li><a href="/account" title="Account" id="current">Account</a></li>
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:										
						<li><a href="/users" title="User Section">Users</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif
 </%def>
 