import React from 'react';
import './BlogPost.css';

interface BlogPostProps {
  title: string;
  date: string;
  content: string;
}

const BlogPost: React.FC<BlogPostProps> = ({ title, date, content }) => {
  return (
    <div className="blog-post">
      <h2>{title}</h2>
      <p className="date">{date}</p>
      <p>{content}</p>
    </div>
  );
};

export default BlogPost;