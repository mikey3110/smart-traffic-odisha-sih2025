# signal_optimizer.py

class RuleBasedSignalOptimizer:
    def __init__(self, green_time=30):
        """
        Initialize the optimizer
        :param green_time: default green signal time (seconds)
        """
        self.green_time = green_time

    def optimize(self, queue_length):
        """
        Simple optimization rule:
        - If queue length > 10, extend green by 10 seconds
        - Else reduce green by 5 seconds (minimum 10 seconds)
        
        :param queue_length: number of vehicles waiting at the signal
        :return: optimized green light duration in seconds
        """
        if queue_length > 10:
            new_time = self.green_time + 10
            print(f"Queue length {queue_length} > 10. Extending green time to {new_time} seconds.")
        else:
            new_time = max(10, self.green_time - 5)
            print(f"Queue length {queue_length} <= 10. Reducing green time to {new_time} seconds.")
        return new_time


def main():
    optimizer = RuleBasedSignalOptimizer()

    # Test different queue lengths
    test_queues = [5, 8, 12, 15, 7]

    for q_len in test_queues:
        optimized_time = optimizer.optimize(q_len)
        print(f"Optimized green light time: {optimized_time} seconds\n")


if __name__ == "__main__":
    main()
