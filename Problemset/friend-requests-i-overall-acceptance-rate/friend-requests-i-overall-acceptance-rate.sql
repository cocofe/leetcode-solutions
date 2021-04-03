
-- @Title: 好友申请 I：总体通过率 (Friend Requests I: Overall Acceptance Rate)
-- @Author: cocofe
-- @Date: 2021-04-03 14:08:45
-- @Runtime: 320 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select round(ifnull(
    (select count(distinct requester_id, accepter_id) from RequestAccepted) /
    (select count(distinct sender_id ,send_to_id) from FriendRequest), 0
    ), 2)  as accept_rate;


