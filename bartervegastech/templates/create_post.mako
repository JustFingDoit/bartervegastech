								<form name="post-job" id="post-job" class="nice" method="post" action="">
								
									<label for="status">Looking to <span class="req">*</span></label>
									<select name="status" id="status">
										<option selected="selected" value="want">post a request</option>
										<option value="offer">offer my services</option>
									</select>
								
									<label for="position">Title <span class="req">*</span></label>
									<input class="expand input-text" id="position" name="title" required="required" maxlength="100" placeholder="e.g. Juggling" type="text">

									<label for="category">Category <span class="req">*</span></label>
									<select name="category" id="category">
										<option selected="selected" value="null">Please choose:</option>
										%for category in categories:
										<option value="${category.id}">${category.category}</option>
										%endfor
									</select>

									<label for="description">Description <span class="req">*</span><span class="note">No HTML</span></label>
									<textarea name="description" id="description" class="expand" placeholder="Include a description of more specifically you have in mind." rows="10" required="required"></textarea>																		
																		
																		
									<label for="howtoapply">And in return... <span class="req">*</span><span class="note">No HTML</span></label>
									<textarea name="inreturn" id="howtoapply" class="expand" placeholder="What would you want or offer in return" rows="4" required="required"></textarea>
									
									<input type="checkbox" name="private" value="true" /> I'd like responses to be private.<br />
																		
									<div id="post-job-submit">
									
										<button type="submit" name="submit-btn" id="job-submit-btn" class="nice blue radius button">Submit</button>
									
									</div> 								
								</form>