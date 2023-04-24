import React, { useEffect, useState } from 'react';
import Post from './Post';
import {List} from '@mui/material';

function PostList() {
  const [posts, setPosts] = useState([]);
  const URL_POST = 'http://localhost:5000/posts'
  useEffect(() => {
    fetch(URL_POST)
      .then(response => response.json())
      .then(data => setPosts(data));
  }, []);

  return (
    <List>
      {posts.map(post => (
        <Post key={post.id} title={post.title} content={post.content} />
      ))}
    </List>
  );
}

export default PostList;