import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';

export default function TeachUsScreen () {
  const navigate = useNavigate();
  return (
  <div>
    <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
    <h2 style={{ maxWidth: '100%' }}>
      TEACH US SCREEN COMING SOON!
    </h2>
  </div>
  )
}