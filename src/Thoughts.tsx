import React from 'react';
import BlogPost from './components/BlogPost';
import './Thoughts.css';

const Thoughts: React.FC = () => {
  const blogPosts = [
    {
      title: 'First Blog Post',
      date: '2023-10-01',
      content: 'This is the content of the first blog post.'
    },
    {
      title: 'Second Blog Post',
      date: '2023-10-02',
      content: 'This is the content of the second blog post.'
    }
  ];

  return (
    <div className="thoughts">
      <h1>Thoughts</h1>
      {blogPosts.map((post, index) => (
        <BlogPost key={index} title={post.title} date={post.date} content={post.content} />
      ))}
    </div>
  );
};

export default Thoughts;