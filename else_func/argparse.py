import argparse

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--file_path', type=str, default='', help='file path')
    parser.add_argument('--save_path', type=str, default='', help='model save path')
    parser.add_argument('--syn_len', type=int, default=100, help='length of synthetic data')

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    
    print("-"*20)
    print("opt: ", opt)
    print("-"*20)
    
    return opt

def main(opt):
    print(1)


if __name__ == "__main__":
    opt = parse_opt()
    main(opt) 
