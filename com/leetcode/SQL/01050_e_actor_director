select actor_id,director_id from (
select actor_id,director_id,count(1) as c
from ActorDirector
group by 1,2
having c>=3) t