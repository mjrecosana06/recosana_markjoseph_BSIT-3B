const users = []; // each { id, email, passwordHash }

module.exports = {
  findByEmail: (email) => users.find(u => u.email === email),
  create: (email, passwordHash) => {
    const user = { id: users.length + 1, email, passwordHash };
    users.push(user);
    return user;
  }
};
