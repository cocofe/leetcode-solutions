
-- @Title: 每个帖子的评论数 (Number of Comments per Post)
-- @Author: cocofe
-- @Date: 2021-04-03 18:09:22
-- @Runtime: 863 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select distinct posts.sub_id as post_id, ifnull(count(distinct comments.sub_id), 0) as number_of_comments from Submissions as posts
left join Submissions as comments
on posts.sub_id = comments.parent_id
where posts.parent_id is null
group by posts.sub_id
order by posts.sub_id

