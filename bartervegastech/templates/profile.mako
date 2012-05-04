						<form name="edit-profile" id="edit-profile-form" class="nice" method="post" action="">
						
							<div class="row">
							
								<div class="six columns">
								
									<label for="profile-company">Username <span class="req">*</span></label>

									<input class="expand input-text" id="profile-company" name="username" placeholder="username" value="${user.username}" maxlength="50" required="required" type="text">
																		
									<label for="profile-website">Website URL </label>
									<input class="expand input-text" id="profile-website" name="website" placeholder="e.g. mysite.com" value="${user.website}" maxlength="100" type="text">
																		
									<label for="profile-tagline">Tag line or motto</label>
									<textarea name="tagline" id="profile-tagline" placeholder="e.g. I make advanced web applications for the masses!" rows="3">${user.tagline}</textarea>
									
									<label for="profile-twitter">Twitter username</label>
									<input class="expand input-text" id="profile-twitter" name="twitter" placeholder="ie. TwitterUser" maxlength="50" value="${user.twitter}" type="text">
									
								</div> 								
								<div class="six columns">
								
									<label for="description">Description</label>
									<textarea name="description" id="profile-tagline" placeholder="ie. We make advanced web applications for the masses!" rows="3">${user.description}</textarea>
									
									<label for="profile-address1">Notifications</label>
									%if user.email_notification == 1:
									<input type="checkbox" name="emailnotification" value="true" checked /> I'd like to be notified of responses by email<br />
									%else:
									<input type="checkbox" name="emailnotification" value="true" /> I'd like to be notified of responses by email<br />
									%endif
									<br /><br /><br /><br />
									<div id="edit-profile-submit-btns">
									
										<button type="submit" name="edit-profile-submit" id="edit-profile-submit" title="Update Profile" class="blue radius button nice">Update Profile</button>
									
									</div> 									
								</div> 								
							</div> 						
						</form>