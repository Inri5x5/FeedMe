import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';

//Temp
import foodPic from '../assets/DummyPhoto.jpg';

export default function RecipeDetailsScreen () {
const navigate = useNavigate();
  return (
  <div className="container">
    <NavigationBarHome style={{ alignSelf: 'start', position: 'absolute' }} isLogin={false}></NavigationBarHome>
    <h1> Indomie </h1>
    <img src={foodPic} alt='foodImage'/>
  </div>
  )
}