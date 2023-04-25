import React, { useEffect, useState } from 'react';
import Post from './Post';
import {List, styled} from '@mui/material';

const CustomList = styled(List)(({ theme }) => ({
  height: 'auto',
}));

function PostList() {
  const [posts, setPosts] = useState([]);
  const URL_POST = 'http://localhost:5000/posts';
  useEffect(() => {
    fetch(URL_POST)
      .then(response => response.json())
      .then(data => setPosts(data));
  }, []);

  return (
    <CustomList>
      {posts.map(post => (
        <Post key={post.post_id} title={post.tittle} content={post.content} creation_date={post.created_at} author={post.user_id} parent_post_id={post.parent_post_id}/>
        // ,console.log(post)
      ))}
    </CustomList>
  );
}

export default PostList;