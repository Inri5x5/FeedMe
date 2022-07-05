import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';

export default function AboutUsScreen () {
  const navigate = useNavigate();
  return (
  <div>
    <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
    <h2 style={{ maxWidth: '100%' }}>
      ABOUT US SCREEN COMING SOON!
    </h2>
  </div>
  )
}