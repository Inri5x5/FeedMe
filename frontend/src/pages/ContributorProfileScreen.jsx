import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';

export default function ContributorProfileScreen () {
  const navigate = useNavigate();
  return (
  <div>
    <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
    <h2 style={{ maxWidth: '100%' , fontFamily: "'Righteous', serif", color: '#FFF3D9', fontSize: '5em'}}>
      CONTRIBUTOR PROFILE SCREEN COMING SOON!
    </h2>
  </div>
  )
}