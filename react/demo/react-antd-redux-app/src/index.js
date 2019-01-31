import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import MenuExample from './components/test/MobileTest';
import NavBarTest from './components/NavBar';


function App() {
    return (
        <NavBarTest />
    );
}

ReactDOM.render(<App />, document.getElementById('app'));
