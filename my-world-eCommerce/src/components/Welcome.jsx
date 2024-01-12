import React from "react";
import "../css/main.css";
import Sammy from "../img/sammy.jpeg";

const Welcome = () => {
  return (
    <>
      <div className="wrapper">
        <h1>Welcome to my app.</h1>
        <p>This is going to be the coolest app in the world!</p>
        <img src={Sammy} alt="Sammy image" width={200} height={200} />
      </div>
    </>
  );
};

export default Welcome;
