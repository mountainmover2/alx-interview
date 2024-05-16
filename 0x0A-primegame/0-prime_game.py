def isWinner(x, nums):
    def sieve(n):
        """ Return a list of primes up to n using Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]
    
    def play_game(n, primes):
        """ Simulate the game for a given n and list of primes """
        numbers = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        
        while True:
            # Find the next prime in the remaining numbers
            prime_found = False
            for prime in primes:
                if prime in numbers:
                    prime_found = True
                    # Remove the prime and its multiples
                    multiples = set(range(prime, n + 1, prime))
                    numbers -= multiples
                    break
            
            if not prime_found:
                # No more primes to remove, the current player loses
                return turn ^ 1  # Return the other player as winner
            
            # Switch turn
            turn ^= 1
    
    # Determine the maximum value in nums
    max_n = max(nums)
    
    # Generate primes up to the maximum number in nums
    primes = sieve(max_n)
    
    # Play each game and determine the winner
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n, primes)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
print(isWinner(5, [2, 5, 1, 4, 3]))  # Output should be "Ben"

