
get_user_url = "https://api.vk.com/method/users.get?user_ids=%(user_id)s&v=5.67&lang=%(lang)s"
get_group_members_url = "https://api.vk.com/method/groups.getMembers?count=0&group_id=%(group_id)s&v=5.67"
message_send_url = "https://api.vk.com/method/messages.send?message=%(message)s&peer_id=%(peer_id)s&v=5.67&access_token=%(access_token)s"
u_message_send_url = "https://api.vk.com/method/messages.send?message=%(message)s&user_id=%(user_id)s&v=5.67&access_token=%(access_token)s"
u_message_send_url = "https://api.vk.com/method/messages.send?message=%(message)s&user_id=%(user_id)s&v=5.67&access_token=%(access_token)s"

wall_post_delete_url = "https://api.vk.com/method/wall.deleteComment?owner_id=%(owner_id)s&comment_id=%(comment_id)s&access_token=%(access_token)s&v=5.67"
 