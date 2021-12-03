# Restart script for eCare(P) application
Use cases:
- bez flagu: pustí sa plná funkcionalita
- flag "orig": ako prvý argument, prehodí sa apache profil (s graceful reštartom) na pôvodný profil
- flag "blue" alebo "green": ako prvý argument, prehodí sa apache profil (s graceful reštartom) podľa farby a prebehne reštart
- flag "norestart": ako druhý argument, prehodia sa iba apache (s graceful reštartom) bez reštartovania strojov
